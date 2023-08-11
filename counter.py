import justpy as jp

def decrement(self,msg):
    val = int(msg.page.count.text)
    val -= 1
    msg.page.count.text = val

def increment(self,msg):
    val = int(msg.page.count.text)
    val += 1
    msg.page.count.text = val    

def counter():
    wp = jp.WebPage()
    container = jp.Div(classes='flex justify-between items-center w-1/4',a=wp)
    
    dec = jp.Button(text="Decrement",classes="rounded-md p-2 bg-red-500", a=container)
    dec.on('click',decrement)
    
    wp.count = jp.H2(text=0,classes="text-xl", a=container)
    
    inc = jp.Button(text="Increment",classes="rounded-md p-2 bg-green-500", a=container)
    inc.on('click',increment)
    return wp
    
jp.justpy(counter,port=8080)
