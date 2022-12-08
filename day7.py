directories, path, curr_dir = {}, [], ""
for cmd in open('input/day7.txt').read().split('\n'):
	if cmd.startswith('$ ls') or cmd.startswith('dir'): continue
	if cmd.startswith('$ cd'):
		new_dir = cmd.split()[2]
		if new_dir == '/':
			directories[new_dir] = 0
			path.append(new_dir)
			curr_dir = new_dir
		elif new_dir == '..':
			path.pop()
			curr_dir = path[-1]
		else:
			curr_dir = curr_dir + new_dir + '/'
			if curr_dir not in directories.keys():
				directories[curr_dir] = 0
				path.append(curr_dir)
	else:
		size = int(cmd.split()[0])
		for i in range(len(path)):
			directories[path[i]] += size
print(f"Part 1: {sum([size for size in directories.values() if size <= 100000])}")
print(f"Part 1: {min([size for size in directories.values() if size >= 30000000 - (70000000 - directories['/'])])}")