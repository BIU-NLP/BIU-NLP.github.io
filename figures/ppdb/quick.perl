while($file = <>) {
    chomp $file;

    if($file =~ m/(^.*)-(figure|table)-\d+.jpeg$/) {
	$path = $1;
	$newfile = $file;
	$newfile =~ s/jpeg/jpg/;
	print "mv $file ../$path/$newfile\n";
    }
}
