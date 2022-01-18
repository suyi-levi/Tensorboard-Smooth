# Tensorboard-Smooth

A script for smoothing the csv data of tensorboard. 

**Smooth function:** 

smoothed_val = weight * last_val + (1 - weight) * current_val

## Environment

- python >= 3.6
- pandas >= 1.2
- numpy >= 1.20

## Run

```python
python smooth.py --input=input_path --output=output_path --weight=smooth_weight
```

## Contact

If you have any questions, please don't hesitite to email to suyi.levi@gmail.com.

