# 预处理生成数据集步骤

1. 生成shapenet数据集对应模型的meta文件
    ```shell
    cd nvdiffrec/data
    python gen_shapenet_meta.py --data_root_dir <path to shapenetcorev1> --save_dir <path to meta file folder dir>
    ```
    默认情况下，我们将meta文件存到 `nvdiffrec/data/shapenet_meta/` 下面，得到 `chair.json` 等文件
2. 然后，利用生成的meta文件进行拟合，得到dmtet的ground truth
    ```shell
    cd ../
    python fit_dmtets.py --config ./configs/res64.json --meta-folder <path to meta file> --out-dir <path to save dir> --index <index of split> --split_size <split size> 
    ```
    其中，`<path to meta file>` 为生成的某个类别的 meta 文件，例如 `./data/shapenet_meta/chair.json`，`<path to save dir>` 为保存数据的位置，**不同类别需要存在不同的文件夹下面**，由于生成速度比较慢，通常我们希望并行执行多个生成任务，假定我们将整个数据集划分成多干个子任务，每个子任务生成 `<split size>` 个，第 `<index of split>` (从0开始) 负责生成 `<index of split> * <split_size> ~ (<index of split>+1) * <split_size>` 个模型的拟合