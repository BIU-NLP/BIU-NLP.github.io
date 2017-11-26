while($line = <>) {
    chomp $line;
    if(!($line =~ m/\(/)) {
	if($line =~ m/(.*)\/.*\s-\s(.*\.pdf)/) {
	    $path = $1;
	    $file = $2;
	    $line =~ s/ /\\ /g;
	    print "mv $line $path/$file\n";
	}
    }
}
