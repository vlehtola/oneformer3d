# --ipc=host needed to avoid docker memory errors
docker run --gpus device=0 --ipc=host -v ~/oneformer3d:/workspace/oneformer3d -it oneformer3d 
echo This may be needed:
echo export PYTHONPATH=/workspace/oneformer3d/

