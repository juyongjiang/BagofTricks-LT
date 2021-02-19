from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from yacs.config import CfgNode as CN


_C = CN()

# ----- BASIC SETTINGS -----
_C.NAME = "default"
_C.OUTPUT_DIR = "/home/cifar10/output"
_C.VALID_STEP = 5
_C.SAVE_STEP = 5
_C.SHOW_STEP = 20
_C.PIN_MEMORY = True
_C.INPUT_SIZE = (224, 224)
_C.COLOR_SPACE = "RGB"
_C.RESUME_MODEL = ""
_C.RESUME_MODE = "all"
_C.EVAL_MODE = False



# ----- DATASET BUILDER -----
_C.DATASET = CN()

# ----- use CAM to generate balanced enhanced datast -----
_C.DATASET.GENERATE_CAM_BASED_DATASET = False
_C.DATASET.USE_CAM_BASED_DATASET = False
_C.DATASET.CAM_DATA_JSON_SAVE_PATH = ''
_C.DATASET.CAM_DATA_SAVE_PATH = ''
_C.DATASET.CAM_NUMBER_THRES = 0

_C.DATASET.DATASET = "IMBALANCEDCIFAR10"
_C.DATASET.ROOT = "/home/cifar10/data"
_C.DATASET.TRAIN_JSON = ""
_C.DATASET.VALID_JSON = ""
_C.DATASET.IMBALANCECIFAR = CN()
_C.DATASET.IMBALANCECIFAR.RATIO = 0.01
_C.DATASET.IMBALANCECIFAR.RANDOM_SEED = 0



_C.NETWORK = CN()
_C.NETWORK.PRETRAINED = False
_C.NETWORK.PRETRAINED_MODEL = ''

# ----- BACKBONE BUILDER -----
_C.BACKBONE = CN()
_C.BACKBONE.TYPE = "res50"
_C.BACKBONE.FREEZE = False
_C.BACKBONE.PRETRAINED_MODEL = ""


# ----- MODULE BUILDER -----
_C.MODULE = CN()
_C.MODULE.TYPE = "GAP"

# ----- CLASSIFIER BUILDER -----
_C.CLASSIFIER = CN()
_C.CLASSIFIER.TYPE = "FC"
_C.CLASSIFIER.BIAS = True


# ----- LOSS BUILDER -----
_C.LOSS = CN()
_C.LOSS.LOSS_TYPE = "CrossEntropy"

_C.LOSS.CostSensitiveCE = CN()
_C.LOSS.CostSensitiveCE.GAMMA = 1.0


_C.LOSS.ClassBalanceCE = CN()
_C.LOSS.ClassBalanceCE.BETA = 0.999

_C.LOSS.ClassBalanceFocal = CN()
_C.LOSS.ClassBalanceFocal.BETA = 0.999
_C.LOSS.ClassBalanceFocal.GAMMA = 0.5

_C.LOSS.CrossEntropyLabelSmooth = CN()
_C.LOSS.CrossEntropyLabelSmooth.EPSILON = 0.1

_C.LOSS.FocalLoss = CN()
_C.LOSS.FocalLoss.GAMMA = 2.0

_C.LOSS.LDAMLoss = CN()
_C.LOSS.LDAMLoss.SCALE = 30.0
_C.LOSS.LDAMLoss.MAX_MARGIN = 0.5

_C.LOSS.CDT = CN()
_C.LOSS.CDT.GAMMA = 0.2

_C.LOSS.SEQL = CN()
_C.LOSS.SEQL.GAMMA = 0.9
_C.LOSS.SEQL.LAMBDA = 0.005



# ----- TRAIN BUILDER -----
_C.TRAIN = CN()
_C.TRAIN.BATCH_SIZE = 32
_C.TRAIN.MAX_EPOCH = 60
_C.TRAIN.SHUFFLE = True
_C.TRAIN.NUM_WORKERS = 8
_C.TRAIN.TENSORBOARD = CN()
_C.TRAIN.TENSORBOARD.ENABLE = True

_C.TRAIN.COMBINER = CN()
_C.TRAIN.COMBINER.TYPE = (
    "default"
)
_C.TRAIN.COMBINER.ALPHA = 1.0

_C.TRAIN.COMBINER.MANIFOLD_MIX_UP = CN()
_C.TRAIN.COMBINER.MANIFOLD_MIX_UP.LOCATION = "pool"

_C.TRAIN.COMBINER.REMIX = CN()
_C.TRAIN.COMBINER.REMIX.KAPPA = 3.0
_C.TRAIN.COMBINER.REMIX.TAU = 0.5

# ----- TRAIN TWO_STAGE_TRAINING SETTING -----
_C.TRAIN.TWO_STAGE = CN()
_C.TRAIN.TWO_STAGE.DRW = False
_C.TRAIN.TWO_STAGE.DRS = False
_C.TRAIN.TWO_STAGE.START_EPOCH = 1

# ----- SAMPLER BUILDER -----
_C.TRAIN.SAMPLER = CN()
_C.TRAIN.SAMPLER.TYPE = "default"

_C.TRAIN.SAMPLER.WEIGHTED_SAMPLER = CN()
_C.TRAIN.SAMPLER.WEIGHTED_SAMPLER.TYPE = "balance"

_C.TRAIN.OPTIMIZER = CN()
_C.TRAIN.OPTIMIZER.TYPE = "SGD"
_C.TRAIN.OPTIMIZER.BASE_LR = 0.001
_C.TRAIN.OPTIMIZER.MOMENTUM = 0.9
_C.TRAIN.OPTIMIZER.WEIGHT_DECAY = 1e-4


_C.TRAIN.LR_SCHEDULER = CN()
_C.TRAIN.LR_SCHEDULER.TYPE = "multistep"
_C.TRAIN.LR_SCHEDULER.LR_STEP = [40, 50]
_C.TRAIN.LR_SCHEDULER.LR_FACTOR = 0.1
_C.TRAIN.LR_SCHEDULER.WARM_EPOCH = 5
_C.TRAIN.LR_SCHEDULER.COSINE_DECAY_END = 0

_C.TRAIN.DISTRIBUTED = False
_C.TRAIN.SYNCBN = False

# testing
_C.TEST = CN()
_C.TEST.BATCH_SIZE = 32
_C.TEST.NUM_WORKERS = 8
_C.TEST.MODEL_FILE = ""

_C.TRANSFORMS = CN()
_C.TRANSFORMS.TRAIN_TRANSFORMS = ("random_resized_crop", "random_horizontal_flip")
_C.TRANSFORMS.TEST_TRANSFORMS = ("shorter_resize_for_crop", "center_crop")

_C.TRANSFORMS.PROCESS_DETAIL = CN()
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_CROP = CN()
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_CROP.PADDING = 4
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_RESIZED_CROP = CN()
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_RESIZED_CROP.SCALE = (0.08, 1.0)
_C.TRANSFORMS.PROCESS_DETAIL.RANDOM_RESIZED_CROP.RATIO = (0.75, 1.333333333)

def update_config(cfg, args):
    cfg.defrost()
    cfg.merge_from_file(args.cfg)
    cfg.merge_from_list(args.opts)

    cfg.freeze()