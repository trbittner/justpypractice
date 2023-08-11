import justpy as jp

# The initial list of items.
items = ['Write Code','Sleep','Have Fun']

def todo_item(item):
    li = jp.Li()
    container = jp.Div(classes='flex m-2 items-center',a=li)
    jp.Button(classes='bg-white border border-blue-400 h-6 w-10 rounded m-1',
        a=container).on('click',finish_item)
    jp.Span(text=item,classes='inline-block text-md',a=container)
    
    return li
    
def todo_list(items):
    o_list = jp.Ol(classes="list-decimal")
    for item in items:
        o_list.add(item)
    return o_list

def add_item(self,msg):
    container = msg.page.components[0]
    
    new_item = todo_item(msg.page.input.value)
    msg.page.input.value = ''
    todo_list = container.last()
    todo_list.add(new_item)

def finish_item(self,msg):
    container = msg.page.components[0]
    todo_list = container.last()
    # This is an li created by todo_item
    for item in todo_list.components:
        id = item.first().first().id
        if self.id == id:
            todo_list.remove_component(item)

def todo():
    wp = jp.WebPage()
    container = jp.Div(classes="bg-gray-200 m-2 padding-1 rounded-sm \
        shadow-lg flex flex-col justify-center items-center w-1/3 m-auto",a=wp)
    jp.H2(text="Todos",classes='text-2xl font-bold',a=container)
    wp.input = jp.Input(placeholder='Add a todo...',
        classes='focus:outline-none p-1 m-2 w-11/12 shadow-lg rounded-md', 
        a=container)
    jp.Button(text='Add',classes='bg-white m-2 p-2 w-1/6 rounded font-bold',
        a=container).on('click',add_item)
    # Build the initial list of todos.  All other updates will be handled via
    # update functions above.
    component_items = [todo_item(item) for item in items]
    container.add(todo_list(component_items))
    return wp

jp.justpy(todo,port=8080)
