import param 
import panel as pn, numpy as np
import panel_highcharts as ph
pn.extension('highgantt')

from datetime import datetime as dt

EPOCH = dt.utcfromtimestamp(0)
configuration = {"title": {"text": ''},
                 "series": [ {"name": "Project 1",
                              "data": [],}
                            ] }

def convert_to_miliseconds(value):
    if not value == "":
        s_dt = dt.strptime(value, "%Y/%m/%d")
        return int((s_dt - EPOCH).total_seconds() * 1000)
    else:
        return None
        # s_dt = dt.strptime(dt.today(), "%Y/%m/%d")
        # return int((s_dt - EPOCH).total_seconds() * 1000)

class ToDoList(param.Parameterized):
    state = param.Dict({})
  
    def adder(self):
        add_input = pn.widgets.TextInput(name='Add item', width=300, placeholder= 'to do list items')
        add_button = pn.widgets.Button(name='+', width=15, button_type='success', align='end')

        def add_item(event):
            if add_input.value not in list(self.state.keys()) and add_input.value != '':
                self.state = { **self.state, add_input.value:(False, None)}
                add_input.value = '' 
        add_button.on_click(add_item)

        @pn.depends(add_input.param.value, watch=True)
        def add_item_from_enter(value):
            if value not in self.state.keys() and value != '':
                self.state = { **self.state, value:(False, None)}
                add_input.value = ''

        return pn.Row(add_input,add_button)

    def get_item_list(self, text, done, dat):
        done = pn.widgets.Checkbox(value=done, width=15, align='end')
        textw = pn.pane.Markdown('### '+ text, width=155, margin=(0, 0, -8, 0), align='end')
        date = pn.widgets.DatetimeRangePicker(width=110, value=dat)
        remove = pn.widgets.Button(name='x', width=15, button_type='danger', align='end')

        @pn.depends(done.param.value, watch=True)
        def update_done(value):
            self.state = {k:(value, v[1]) if k==text else v for k,v in self.state.items() }

        @pn.depends(date.param.value, watch=True)
        def update_date(value):
            self.state = {k:(v[0], value) if k==text else v for k,v in self.state.items() }

        def delete_item(event):
            # if k != text:
            print ('deleting', event, text )
            self.state = {k:v for k,v in self.state.items() if k!=text}
        remove.on_click(delete_item)

        return pn.Row(done, textw, date, remove)

    def view_list(self):
        return pn.Column(*[self.get_item_list(k,v[0], v[1]) for k,v in self.state.items()])


class Gantt(param.Parameterized):
    parent = param.Parameter()

    def __init__(self, **params):
        super().__init__(**params)
        self.chart = ph.HighGantt(object=configuration, sizing_mode="stretch_width", 
                                height=300)

    @param.depends('parent.state', watch=True)
    def update_chart(self):
        tasks = []
        
        for k, v in self.parent.state.items():
            ide, name = np.random.randint(1000), k
            if v[1] is not None:
                start = int((v[1][0]- dt.utcfromtimestamp(0)).total_seconds())*1000 
                end = int((v[1][1]- dt.utcfromtimestamp(0)).total_seconds())*1000 
            else:
                start, end = None, None
            tasks.append(({'id':ide, 'name':name, 'start':start,'end':end}))
        self.chart.object_update =  {'series':{"name":"Project 1","data":tasks}}
        print ('cal',  {'series':{"name":"Project 1","data":tasks}})


todo = ToDoList()
gantt = Gantt(parent=todo)

header = pn.Row(pn.Spacer(sizing_mode='stretch_width'),
            pn.pane.PNG('lis.png', width = 600),
            pn.Spacer(sizing_mode='stretch_width'),sizing_mode='stretch_width')

body = pn.Row(pn.Column(todo.adder,
                todo.view_list,
                todo.param ),
    gantt.chart,
    )
    
pn.Column(header, 
        '## Project1', body, 
        sizing_mode='stretch_width').servable()