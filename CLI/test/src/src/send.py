
from __future__ import unicode_literals
from pytg.receiver import Receiver  # get messages
from pytg.sender import Sender  # send messages, and other querys.
from pytg.utils import coroutine
import datetime as dt
from pytg import Telegram
import sys
import timeit
tg = Telegram(
    telegram="../tg/bin/telegram-cli",
    pubkey_file="../tg/tg-server.pub")
receiver = tg.receiver
sender = tg.sender

#To measure the time interval between two points
start = 0.0
end = 0.0



def main():
    # get a Receiver instance, to get messages.
    #receiver = Receiver(host="localhost", port=4458)

    # get a Sender instance, to send messages, and other querys.
    #sender = Sender(host="localhost", port=4458)

    # start the Receiver, so we can get messages!
    receiver.start()  # note that the Sender has no need for a start function.

    # add "example_function" function as message listener. You can supply arguments here (like sender).
     # now it will call the example_function and yield the new messages.
    #receiver.message(example_function(sender))
    receiver.message(example_function(sender))
    
    # please, no more messages. (we could stop the the cli too, with sender.safe_quit() )
    receiver.stop()

    # continues here, after exiting while loop in example_function()
    print("I am done!")

    # the sender will disconnect after each send, so there is no need to stop it.
    # if you want to shutdown the telegram cli:
    # sender.safe_quit() # this shuts down the telegram cli.
    # sender.quit() # this shuts down the telegram cli, without waiting for downloads to complete.


# this is the function which will process our incoming messages
@coroutine
def example_function(sender):  # name "example_function" and given parameters are defined in main()
    QUIT = False
    ADMIN_ID = 10717954
    print "This is the Sender"
    try:
        start = dt.datetime.now()
        sender.send_msg(u'user#197837846', u"Ping Ping Ping Ping Ping Ping Ping Ping")
        print "Sent a message"
        while not QUIT:  # loop for messages
            sender.status_online()  # so we will stay online.
            # (if we are offline it might not receive the messages instantly,
            #  but eventually we will get them)

            msg = (yield)  # it waits until the generator has a has message here.
            if msg.event != "message":
                continue  # is not a message.
            if msg.own:  # the bot has send this message.
                continue  # we don't want to process this message.
            if msg.text == None:  # we have media instead.
                continue  # and again, because we want to process only text message.
            # Everything in ptg2 will be unicode. If you use python 3 thats no problem,
            # just if you use python 2 you have to be carefull! (better switch to 3)
            # for convinience of py2 users there is a to_unicode(<string>) in pytg.encoding
            # for python 3 the using of it is not needed.
            # But again, use python 3, as you have a chat with umlaute and emojis.
            # This WILL brake your python 2 code at some point!
            if msg.text == u"Pong!":
               print "Got a message back"
               end = dt.datetime.now()
               print start, end
               print (end.microsecond - start.microsecond)/1e3
               QUIT = True 
    except GeneratorExit:
        # the generator (pytg) exited (got a KeyboardIterrupt).
        pass
    except KeyboardInterrupt:
        # we got a KeyboardIterrupt(Ctrl+C)
        sys.exit()
    else:
        # the loop exited without exception, becaues _quit was set True
        pass
## program start here ##
if __name__ == '__main__':
    main()  # executing main function.
    # Last command of file (so everything needed is already loaded above)
