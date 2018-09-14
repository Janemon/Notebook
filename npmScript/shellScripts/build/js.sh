for file in ./js/*.js
do
      ./node_modules/uglify-es/bin/uglifyjs $file --mangle > dist/js/$(basename $file)
done

