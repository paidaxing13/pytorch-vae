import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--gpu', type=int, default=7)
parser.add_argument('--seed', type=int, default=42)
parser.add_argument('--log_interval', type=int, default=500)
parser.add_argument('--figs', action='store_true')

parser.add_argument('--dataset_dir', type=str, default='')
parser.add_argument('--dataset', type=str, default='stochmnist',
                    choices=['stochmnist', 'omniglot', 'fixedmnist'])
parser.add_argument('--batch_size', type=int, default=20) # iwae uses 20
parser.add_argument('--test_batch_size', type=int, default=64)
parser.add_argument('--mean_num', type=int, default=1) # M in "tighter variational bounds...". Use 1 for vanilla vae
parser.add_argument('--importance_num', type=int, default=1) # k of iwae. Use 1 for vanilla vae
parser.add_argument('--epochs', type=int, default=100000) # iwae uses 3280
parser.add_argument('--learning_rate', type=float, default=1e-3)
parser.add_argument('--run', type=int, default=1)

parser.add_argument('--no_analytic_kl', action='store_true')
parser.add_argument('--h_dim', type=float, default=200)
parser.add_argument('--z_dim', type=float, default=50)
parser.add_argument('--beta', type=float, default=1)

def get_args():
    args = parser.parse_args()

    args.exp_name = 'm{}_k{}'.format(args.mean_num, args.importance_num)
    if args.dataset != 'stochmnist': args.exp_name += '_{}'.format(args.dataset)
    if args.run != 1: args.exp_name += '_run{}'.format(args.run)
    if args.batch_size != 20: args.exp_name += '_bs{}'.format(args.batch_size)
    if args.h_dim != 200: args.exp_name += '_h{}'.format(args.h_dim)
    if args.z_dim != 50: args.exp_name += '_z{}'.format(args.z_dim)
    if args.learning_rate != 1e-3: args.exp_name += '_z{}'.format(args.learning_rate)
    if args.beta != 1: args.exp_name += '_beta{}'.format(args.beta)
    if args.no_analytic_kl: args.exp_name += '_noanalytic'

    args.figs_dir = 'figs/{}'.format(args.exp_name)
    args.out_dir = 'result/{}'.format(args.exp_name)
    if not os.path.exists(args.out_dir):
        os.makedirs(args.out_dir)
    if not os.path.exists(args.figs_dir):
        os.makedirs(args.figs_dir)

    if args.dataset in ['fixedmnist', 'stochmnist', 'omniglot']:
        args.x_dim = 784
    return args

