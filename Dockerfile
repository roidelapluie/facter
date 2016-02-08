FROM centos:7

MAINTAINER Julien Pivotto <roidelapluie@inuits.eu>

RUN mkdir /workspace
COPY . /workspace

RUN yum install -y /usr/bin/spectool /usr/bin/rpmbuild /usr/bin/yum-builddep


RUN useradd bob
RUN mkdir -p /home/bob/rpmbuild/SOURCES

RUN find /workspace/ -maxdepth 1 -type f -exec cp -v '{}' /home/bob/rpmbuild/SOURCES ';'

RUN yum install -y epel-release
RUN yum install -y https://github.com/CfgMgmtSIG/cmake/releases/download/3.4.3-3/cmake-3.4.3-3.el7.centos.x86_64.rpm


RUN yum install -y centos-release-scl-rh

RUN spectool -C /home/bob/rpmbuild/SOURCES -g /workspace/facter.spec
RUN yum-builddep -y /workspace/facter.spec

RUN chown -R bob: /home/bob /workspace

RUN su - bob -c 'scl enable devtoolset-3 "rpmbuild -ba /workspace/facter.spec"'

VOLUME /artifacts
