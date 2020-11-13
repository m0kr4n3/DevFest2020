original="`pwd`/"
while [[ ! -f "FinalWork.zip" ]]
do
	unzip -n *.zip
	cd */
done
unzip -n FinalWork.zip
cp Congratulations.pdf $original
cd $original
rm -r unZipMe
xdg-open Congratulations.pdf
