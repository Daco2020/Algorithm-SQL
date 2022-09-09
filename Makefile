tistory-upload:
	git add .
	git commit -m "upload"
	git push origin main
	sleep 60
	git pull origin main
