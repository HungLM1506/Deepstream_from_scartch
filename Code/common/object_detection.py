import pyds
from gi.repository import Gst, GObject
import gi
gi.require_version('Gst', '1.0')


PGIE_CLASS_ID_VEHICLE = 0
PGIE_CLASS_ID_BICYCLE = 1
PGIE_CLASS_ID_PERSON = 2
PGIE_CLASS_ID_ROADSIGN = 3


def osd_sink_pad_buffer_probe(pad, info, u_data):
    frame_number = 0
    obj_counter = {
        PGIE_CLASS_ID_VEHICLE: 0,
        PGIE_CLASS_ID_PERSON: 0,
        PGIE_CLASS_ID_BICYCLE: 0,
        PGIE_CLASS_ID_ROADSIGN: 0
    }
    num_rects = 0

    gst_buffer = info.get_buffer()
    if not gst_buffer:
        return
    batch_meta = pyds.gst_buffer_get_nvds_batch_meta(hash(gst_buffer))
    l_frame = batch_meta.frame_meta_list
    while l_frame is not None:
        try:
            frame_meta = pyds.NvDsObjectMeta.cast(l_frame.data)
        except StopIteration:
            break
    frame_number = frame_meta.frame_num
    num_rects = frame_meta.num_obj_meta
