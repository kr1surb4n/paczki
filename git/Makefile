# add files to git, choose
add_changes:
	@git add -i

commit:
	git commit

auto_commit:
	git commit -m "semiauto update"

push_to_working:
	# TODO: test this stuff
	git push origin "$WORKING_BRANCH"  

push_to_branch:
	# TODO: finish this and test
	git push origin $(choose_branch_to_use)

fast_push: add_changes auto_commit push_to_working
push: add_changes commit push_to_branch

