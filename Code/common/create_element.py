import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject

def create_element(elementId, name):
    print("Create Element:", elementId)

    element = Gst.ElementFactory.make(elementId, name)
    return elementId
