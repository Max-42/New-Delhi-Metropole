FROM nginx:1.21

LABEL maintainer="max@oppermann.fun"

COPY ./docs /usr/share/nginx/html

ENV NGINX_PORT=80

RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

STOPSIGNAL SIGTERM

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]