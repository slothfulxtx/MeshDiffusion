import os.path as osp
import os
import json
import argparse

id2cat = {
    '03001627': 'chair',
    '02691156': 'airplane',
    '02958343': 'car',
    '04090263': 'rifle',
    '04379243': 'table'
}

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--data_root_dir', default='/home/tianxing/nas/ShapeNet/ShapeNetCore.v1/', type=str)
    parser.add_argument(
        '--save_dir', default='./shapenet_meta', type=str)
    args = parser.parse_args()

    os.makedirs(args.save_dir, exist_ok=True)

    for cat_id in id2cat:

        cat_name = id2cat[cat_id]
        if osp.exists(osp.join(args.save_dir, '%s.json' % cat_name)):
            continue
        root_dir = osp.join(args.data_root_dir, cat_id)
        model_ids = sorted(os.listdir(root_dir))
        model_dirs = [osp.join(root_dir, i, 'model.obj') for i in model_ids]

        with open(osp.join(args.save_dir, '%s.json' % cat_name), 'w') as f:
            json.dump(model_dirs, f)
