import argparse


class Parser:
    def __init__(self, mode):
        self.parser = argparse.ArgumentParser(description='Pytorch Image Classification (github.com/unique-chan)')
        if mode == 'train':
            self.add_arguments_for_train()
        elif mode == 'test':
            self.add_arguments_for_test()
        self.add_default_arguments()

    def add_default_arguments(self):
        self.parser.add_argument('--network_name', type=str, 
                                 help='network name')
        self.parser.add_argument('--dataset_dir', type=str, 
                                 help='dataset path')
        self.parser.add_argument('--batch_size', default=128, type=int, 
                                 help='batch_size (default: 128)')
        self.parser.add_argument('--mean', default="(0.485, 0.456, 0.456)", type=str,
                                 help='train mean (default: "(0.485, 0.456, 0.456)")')
        self.parser.add_argument('--std', default="(0.229, 0.224, 0.225)", type=str,
                                 help='train std (default: "(0.229, 0.224, 0.225)")')
        self.parser.add_argument('--auto_mean_std', action='store_true',
                                 help='Compute and use train mean/std.'
                                      ' (instead of setting values of [--mean] and [--std])')
        self.parser.add_argument('--transform_list_name', default='', type=str,
                                 help='if you want to use your own transform list, set this value. '
                                      '(See __init__.py and README.md)')
        self.parser.add_argument('--gpu_index', default=0, type=int,
                                 help="[gpu_index = -1]: cpu, [gpu_index >= 0]: gpu")
        self.parser.add_argument('--store_logits', action='store_true',
                                 help='store the output distributions per each epoch for all images (*.csv)')

    def add_arguments_for_train(self):
        self.parser.add_argument('--lr', default=0.1, type=float, 
                                 help='initial learning rate (default: 0.1)')
        self.parser.add_argument('--epochs', default=1, type=int, 
                                 help='epochs (default: 1)')
        self.parser.add_argument('--lr_step', default="[100, 150]", type=str,
                                 help='learning rate step decay milestones (default: "[100, 150]")')
        self.parser.add_argument('--lr_step_gamma', default=0.1, type=float,
                                 help='learning rate step decay gamma (default: 0.1)')
        self.parser.add_argument('--store_weights', action='store_true',
                                 help='store the best model weights (*.pt) during training')
        self.parser.add_argument('--store_loss_acc_log', action='store_true',
                                 help='store the training progress log in terms of loss and accuracy (*.csv)')
        self.parser.add_argument('--tag', type=str, 
                                 help='tag name for current experiment')

    def add_arguments_for_test(self):
        pass
