Suffixes={1000:['KB','MB','TB','PB','EB','ZB','YB'],
		  1024:['KiB','MiB','GiB','TiB','PiB','EiB','ZiB','YiB']}
def approximate_size(size,a_kilobyte_is_1024_byte=True):
	if size < 0:
		raise ValueError('Number is non-negitive')
		
	multiple = 1024 if a_kilobyte_is_1024_byte else 1000

	for suffix in Suffixes[multiple]:
		size /= multiple
		if size < multiple:
			return '{0:1f} {1}'.format(size, suffix)
	raise ValueError('Number is too large')

if __name__=='__main__':
	print(approximate_size(1024**4, False))
	print(approximate_size(1024**4))
