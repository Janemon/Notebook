for file in styles/*.css
do
   cssmin $file > dist/styles/$(basename $file)
done
