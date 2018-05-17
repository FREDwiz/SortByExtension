per ogni (file.dir){
	
	check(.*)
	if(.* exist)
		move(cur.file, dir /.*)
	else
		create(dir /.*)
		move(cur.file, dir /.*)
	}