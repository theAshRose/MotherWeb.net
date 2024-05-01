# nginx/Dockerfile

FROM nginx:stable-alpine

COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80 443 5000

CMD ["nginx", "-g", "daemon off;"]
# CMD ["sh", "-c", "until ping -c1 flaskDB >/dev/null 2>&1; do echo waiting for flaskDB; sleep 1; done; nginx -g 'daemon off;'"] 
