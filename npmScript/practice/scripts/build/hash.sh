# 给图片资源加上版本号，并且替换引用
#hashmark -c dist -r -l 8 './**/*.{png,jpg}' '{dir}/{name}.{hash}{ext}' | replaceinfiles -S -s './dist/**/*.css' -d '{dir}/{base}'

# 给 js、css 资源加上版本号，并且替换引用
#hashmark -c dist -r -l 8 './**/*.{css,js}' '{dir}/{name}.{hash}{ext}' | replaceinfiles -S -s './*.html' -d './dist/index.html'



hashmark -c dist -r -l 8 './**/*.{css,js}' '{dir}/{name}.{hash}{ext}' | replaceinfiles -S -s './*.html' -d './dist/index.html'

hashmark -c dist -r -l 8 './**/*.{png,jpg}' '{dir}/{name}.{hash}{ext}' >| temp

cat temp | replaceinfiles -S -s './dist/**/*.css' -d '{dir}/{base}'

cat temp | replaceinfiles -S -s './dist/index.html' -d './dist/index.html'

rm -f temp

