for file in ./styles/*.scss
do
    sass $file:styles/$(basename $file .scss).css --style expanded
done
