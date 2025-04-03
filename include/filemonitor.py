import pyinotify
from loguru import logger


class FileEventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self,event):
        message=f"New file created: {event.pathname}"
        print(message) 
        logger.warning(message)

    def process_IN_DELETE(self,event):
        message=f"File deleted: {event.pathname}"
        print(message)
        logger.critical(message)

    def process_IN_MODIFY(self,event):
        message=f"File modified: {event.pathname}"
        print(message)
        logger.warning(message)

def monitor(files):
    logger.add("filechanges.log",rotation="10 MB",level="WARNING")
    wm=pyinotify.WatchManager()
    mask=pyinotify.IN_CREATE | pyinotify.IN_DELETE | pyinotify.IN_MODIFY
    handler=FileEventHandler()
    notifier=pyinotify.Notifier(wm,handler)


    for file in files:
        wm.add_watch(file,mask)
    notifier.loop()
def viewlog():
     f=open("filechanges.log","r")
     logs=f.read()
     print(logs)

