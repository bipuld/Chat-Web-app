import asyncio
import json

from channels.consumer import AsyncConsumer,SyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
from asgiref.sync  import async_to_sync
from channels.db import database_sync_to_async
# from app.models import Chat,Group

# from app.models import Chat,Group
class MyAsyncConsumer(AsyncConsumer):

    async def websocket_connect(self,event):
        print("Connection Established 0",event)
        print("Channels Layers default from the project",self.channel_layer , (self.channel_name))
        self.GroupChat=self.scope['url_route']['kwargs']['chat_group']
        await self.channel_layer.group_add(self.GroupChat,self.channel_name) #creating the grup with multiple instances
        await self.send(
            # '''this is a websocket connection and connection is Continuos without being disconnected'''
            {
                'type':'websocket.accept',
            }
        )

    async def websocket_receive(self,event):
        print("Message received Details",event)
        print("Message received from Client",event['text'],type(event['text']))
        data=json.loads(event['text'])
        # group=await database_sync_to_async(Group.objects.get)(group=self.GroupChat) #find group object
        #create New Chat objects
        # chats=Chat(
        #     content=data['msg'],
        #     group_name=group
        # )
        # await database_sync_to_async(chats.save)()
        await self.channel_layer.group_send(self.GroupChat,{
            'type':'chat.message',
            'message':event['text']
        })
    async def chat_message(self,event):
            print(event)
            print(event['message'])
            print(type(event['message']))
            await self.send({
                "type":'websocket.send', #this message first receive from the Client and then again it is same pass to the server
                "text":event['message']
            })
        
            
    # async def websocket_receive(self,event):
    #     # print("Message Received 1",event)
    #     # print("Your message is the  2",event)
    #     print(event['text']) 
    #     for i in range(10):
    #         await self.send({
    #             'type': 'websocket.send',
    #             'text': str(i)
    #         })
    #         await asyncio.sleep(1)

        

    async def websocket_disconnect(self,event):
        print("Terminated",event)
        print("WEBSOCKET DISCARDED",self.channel_name)
        print("WEBSOCKET DISCARDED layer",self.channel_layer) #get default nCHANNEL_LAYER NAME  
        self.channel_layer.group_discard(self.GroupChat,self.channel_name)
        raise StopConsumer()
 
# class MySyncConsumer(SyncConsumer):
    
#     def websocket_connect(self,event):
#         '''this basically establish a connection to the websocket'''
#         print("connected",event)
#         self.send({
#             'type':'websocket.accept',
#         })

#     def websocket_receive(self,event):
#         print("Message Received",event)
#         print("Your Messages Received",event['text']) #this message is send by the Client to server and Display it
#         for i in range(50):
#             self.send(
#                 {
#                     'type':'websocket.send',#this message is send by the server to the client
#                     # 'text':"message sent to server to client"
#                     'text':str(i)
#                 })
#             sleep(i)
        
#     def websocket_disconnect(self,event):
#         print("Terminated",event)
#         raise StopConsumer()



# import asyncio
# import json

# from channels.consumer import AsyncConsumer,SyncConsumer
# from channels.exceptions import StopConsumer
# from time import sleep
# from asgiref.sync  import async_to_sync
# from app.models import Group,Chat
# from channels.db import database_sync_to_async
# # from app.models import Chat,Group
# class MyAsyncConsumer(AsyncConsumer):

#     async def websocket_connect(self,event):
#         print("Connection Established 0",event)
#         print("Channels Layers default from the project",self.channel_layer , (self.channel_name))
#         self.GroupChat=self.scope['url_route']['kwargs']['chat_group']
#         await self.channel_layer.group_add(self.GroupChat,self.channel_name) #creating the grup with multiple instances
#         await self.send(
#             # '''this is a websocket connection and connection is Continuos without being disconnected'''
#             {
#                 'type':'websocket.accept',
#             }
#         )

#     async def websocket_receive(self,event):
#         print("Message received Details",event)
#         print("Message received from Client",event['text'],type(event['text']))
#         data=json.load(event['text'])
#         group=await database_sync_to_async(Group.objects.get)(group=self.GroupChat) #find group object
#         #create New Chat objects
#         chats=Chat(
#             content=data['msg'],
#             group_name=group
#         )
#         await database_sync_to_async(chats.save)()
#         await self.channel_layer.group_send(self.GroupChat,{
#             'type':'chat.message',
#             'message':event['text']
#         })
#     async def chat_message(self,event):
#             print(event)
#             print(event['message'])
#             print(type(event['message']))
#             await self.send({
#                 "type":'websocket.send', #this message first receive from the Client and then again it is same pass to the server
#                 "text":event['message']
#             })
        
            
#     # async def websocket_receive(self,event):
#     #     # print("Message Received 1",event)
#     #     # print("Your message is the  2",event)
#     #     print(event['text']) 
#     #     for i in range(10):
#     #         await self.send({
#     #             'type': 'websocket.send',
#     #             'text': str(i)
#     #         })
#     #         await asyncio.sleep(1)

        

#     async def websocket_disconnect(self,event):
#         print("Terminated",event)
#         print("WEBSOCKET DISCARDED",self.channel_name)
#         print("WEBSOCKET DISCARDED layer",self.channel_layer) #get default nCHANNEL_LAYER NAME  
#         self.channel_layer.group_discard(self.GroupChat,self.channel_name)
#         raise StopConsumer()
