{
	'repo_type' : 'git',
	'url' : 'https://bitbucket.org/multicoreware/x265_git',
	'folder_name': 'x265_multilib_12_git',
	'depth_git': 0,
	'source_subfolder' : '_build',
	'configure_options' : 
		'../source {cmake_prefix_options} '
		'-DCMAKE_AR={cross_prefix_full}ar '
		'-DENABLE_ASSEMBLY=ON '
		'-DHIGH_BIT_DEPTH=ON '
		'-DEXPORT_C_API=OFF '
		'-DENABLE_SHARED=OFF '
		'-DENABLE_CLI=OFF '
		'-DMAIN12=ON '
		'-DCMAKE_INSTALL_PREFIX={offtree_prefix}/libx265_12bit'
	,
	'run_post_install' : [
		'mv -fv "{offtree_prefix}/libx265_12bit/lib/libx265.a" "{offtree_prefix}/libx265_12bit/lib/libx265_main12.a"'
	],
	'conf_system' : 'cmake',
	'_info' : { 'version' : None, 'fancy_name' : 'x265 (library (12))' },
}