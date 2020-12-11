# resized_trashnet
trashnet resized to [64x64|96x96] [rgb|grayscale]

original dataset from [garythung](https://github.com/garythung/trashnet)

## description
original dataset's aspect ratio is 4:3.

This dataset contains cropped center square of it.

`dataset-resized-*` and `*` are exactly the same.

`dataset-resized-*` are there just for compatibility.

* used Pillow for resizing
* format = `png`
* resizing filter = `LANCZOS`

## to download original dataset
`./gdrive_download.sh 1c4wiLZkR_Qs1OQmJ521yZRWgySq502WI`

## `*s.tar.gz` files
`*s.tar.gz` files are sorted ones, such as following;
* vinyl (film) type plastics are removed.
* trash type is removed, except for two paper cups and two plastic yogurt containers)

