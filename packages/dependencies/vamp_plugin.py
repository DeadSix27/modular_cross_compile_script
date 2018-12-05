{
	'repo_type' : 'archive',
	'download_locations' : [
		{ 'url' : 'https://raw.githubusercontent.com/DeadSix27/python_cross_compile_script/master/sources/vamp-plugin-sdk-2.7.1.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c6fef3ff79d2bf9575ce4ce4f200cbf219cbe0a21cfbad5750e86ff8ae53cb0b' }, ], },
		{ 'url' : 'https://code.soundsoftware.ac.uk/attachments/download/2206/vamp-plugin-sdk-2.7.1.tar.gz', 'hashes' : [ { 'type' : 'sha256', 'sum' : 'c6fef3ff79d2bf9575ce4ce4f200cbf219cbe0a21cfbad5750e86ff8ae53cb0b' }, ], },
	],
	'run_post_patch' : [
		'cp -fv build/Makefile.mingw64 Makefile',
	],
	'patches' : [
		('vamp/vamp-plugin-sdk-2.7.1.patch','-p0'), #They rely on M_PI which is gone since c99 or w/e, give them a self defined one and hope for the best.
	],
	'build_options' : '{make_prefix_options} sdkstatic', # for DLL's add 'sdk rdfgen'
	'needs_make_install' : False, # doesnt s support xcompile installing
	'run_post_build' : [ # lets install it manually then I guess?
		'cp -fv libvamp-sdk.a "{target_prefix}/lib/"',
		'cp -fv libvamp-hostsdk.a "{target_prefix}/lib/"',
		'cp -frv vamp-hostsdk/ "{target_prefix}/include/"',
		'cp -frv vamp-sdk/ "{target_prefix}/include/"',
		'cp -frv vamp/ "{target_prefix}/include/"',
		'cp -fv pkgconfig/vamp.pc.in "{target_prefix}/lib/pkgconfig/vamp.pc"',
		'cp -fv pkgconfig/vamp-hostsdk.pc.in "{target_prefix}/lib/pkgconfig/vamp-hostsdk.pc"',
		'cp -fv pkgconfig/vamp-sdk.pc.in "{target_prefix}/lib/pkgconfig/vamp-sdk.pc"',
		'sed -i.bak \'s/\%PREFIX\%/{target_prefix_sed_escaped}/\' "{pkg_config_path}/vamp.pc"',
		'sed -i.bak \'s/\%PREFIX\%/{target_prefix_sed_escaped}/\' "{pkg_config_path}/vamp-hostsdk.pc"',
		'sed -i.bak \'s/\%PREFIX\%/{target_prefix_sed_escaped}/\' "{pkg_config_path}/vamp-sdk.pc"',
	],
	'update_check_url' : { 'url' : 'https://vamp-plugins.org/develop.html', 'type' : 'httpregex', 'regex' : r'.*<ul><li>Download the <b>Vamp plugin SDK<\/b> \(version (?P<version_num>[\d.]+)\):.*' },
	'_info' : { 'version' : '2.7.1', 'fancy_name' : 'vamp-plugin-sdk' },
}