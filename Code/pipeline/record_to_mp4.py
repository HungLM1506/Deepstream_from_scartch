from common.create_element import create_element
from common.bus_call import bus_call
from common.is_aarch_64 import is_aarch64
from gi.repository import GObject, Gst
import gi
import argparse
import sys
sys.path.append('../')

gi.require_version('Gst', '1.0')


def main():

    # Standard GStreamer initialization
    Gst.debug_set_active(True)
    Gst.debug_set_default_threshold(4)
    GObject.threads_init()
    Gst.init(None)

    pipeline = Gst.Pipeline()

    source = create_element("nvarguscamerasrc", "camera-source")
    sink = create_element("nvoverlaysink", "overlay")

    source.set_property('sensor-id', 0)

    pipeline.add(source)
    pipeline.add(sink)

    source.link(sink)

    loop = GObject.MainLoop()
    bus = pipeline.get_bus()
    bus.add_signal_watch()
    bus.connect("message", bus_call, loop)

    pipeline.set_state(Gst.State.PLAYING)

    try:
        loop.run()
    except:
        pass

    # Cleanup
    pipeline.set_state(Gst.State.NULL)


if __name__ == "__main__":
    sys.exit(main())
