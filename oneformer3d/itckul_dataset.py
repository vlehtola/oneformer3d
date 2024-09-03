from mmdet3d.registry import DATASETS
from mmdet3d.datasets.itckul_dataset import ITCKULDataset


@DATASETS.register_module()
class ITCKULSegDataset_(ITCKULDataset):


METAINFO = {
    'classes': ('ceiling', 'floor', 'wall', 'beam', 'column', 'window', 'door',
                'table', 'chair', 'sofa', 'bookcase', 'board', 'clutter', 'stair', 'unlabeled'),
    'palette': [[0, 255, 0], [0, 0, 255], [0, 255, 255], [255, 255, 0],
                [255, 0, 255], [100, 100, 255], [200, 200, 100],
                [170, 120, 200], [255, 0, 0], [200, 100, 100],
                [10, 200, 100], [200, 200, 200], [50, 50, 50], [0, 250, 0], [0, 0, 0]],
    'seg_valid_class_ids': tuple(range(15)),  # Include the index for the 'unlabeled' class
    'seg_all_class_ids': tuple(range(15))  
    }
