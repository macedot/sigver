from .gpds import GPDSDataset
from .mcyt import MCYTDataset
from .cedar import CedarDataset
from .mine import MineDataset
from .brazilian import BrazilianDataset, BrazilianDatasetWithoutSimpleForgeries

available_datasets = {'gpds': GPDSDataset,
                      'mcyt': MCYTDataset,
                      'cedar': CedarDataset,
                      'mine': MineDataset,
                      'brazilian': BrazilianDataset,
                      'brazilian-nosimple': BrazilianDatasetWithoutSimpleForgeries}
