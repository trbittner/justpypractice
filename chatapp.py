import justpy as jp

from enum import Enum
import asyncio
import time


Statement=Enum('Statement',['QUESTION','ANSWER'])
chatbot_answer = "I don't know!"

async def answer(self,msg):
    container = msg.page.components[0]
    
    container.add_component(statement(msg.page.input.value,Statement.QUESTION),
        len(container.components) - 1)
    msg.page.input.value = ''
        
    answer = statement("",Statement.ANSWER)
    
    container.add_component(answer,
        len(container.components) - 1)
        
    for i in range(len(chatbot_answer)+1):
        await msg.page.update()
        time.sleep(.1)
        answer.text = ''.join(chatbot_answer[:i])
    
def statement(text,stmt_type):
    base_classes=' p-3 rounded-lg my-2 shadow-md'
    classes='text-right bg-blue-200 self-end' if stmt_type == Statement.QUESTION \
        else 'text-left bg-blue-400 self-start'
    
    div = jp.Div(text=text,classes=classes + base_classes)
    return div

def chatapp():
    wp = jp.WebPage()
    container = jp.Div(classes="flex flex-col w-1/2 m-auto",a=wp)
    action_bar = jp.Div(classes="flex justify-center",a=container)
    wp.input = jp.Input(placeholder='Ask a question',
        classes='focus:outline-none border border-gray-300 p-1 mr-2 w-11/12 shadow-lg rounded-md', 
        a=action_bar)
    jp.Button(text='Ask',classes='bg-gray-200 p-2 rounded',a=action_bar).on('click',answer)
    return wp
    
jp.justpy(chatapp,port=8080)
