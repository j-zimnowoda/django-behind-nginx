FROM nginx:1.15.9-alpine
EXPOSE 80

RUN rm /etc/nginx/conf.d/default.conf
COPY ./ingress.conf /etc/nginx/conf.d/

CMD ["nginx", "-g", "daemon off;"]
