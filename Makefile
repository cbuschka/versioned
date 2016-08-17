PACKAGE_NAME=version-utils
PACKAGE_VERSION=2
PACKAGE_ARCH=all

target:	prepare copy process fix_perms package

prepare:
	rm -r ./build; \
	if [ ! -d "./build/" ]; then \
		mkdir ./build/; \
	fi

copy:
	cp -R src/* ./build/

process:
	sed -i "s,Package: .*,Package: $(PACKAGE_NAME)," build/DEBIAN/control
	sed -i "s,Version: .*,Version: $(PACKAGE_VERSION)," build/DEBIAN/control
	sed -i "s,Installed-Size: .*,Installed-Size: $(du -sb build/ | cut -f 1)," build/DEBIAN/control

package:
	dpkg -b dist ./build/${PACKAGE_NAME}-${PACKAGE_VERSION}_${PACKAGE_ARCH}.deb

fix_perms:
	chmod 755 build/DEBIAN/*; \
	chmod 644 build/DEBIAN/control; \
	chmod -R a-s build/DEBIAN/*;


#deploy: upload remote_create_symlinks remote_update_index
#
#upload:
#	scp "build/${PACKAGE_NAME}-${PACKAGE_VERSION}_${PACKAGE_ARCH}.deb" "root@debbi:/var/local/nginx/deploy.arcusx.lan/htdocs/debian/pool/"
#
#remote_create_symlinks:
#	ssh root@debbi "cd /var/local/nginx/deploy.arcusx.lan/htdocs/debian/dists/arcusx/stable/binary-amd64;ln -fs ../../../../pool/arcusx-* ."
#
#remote_update_index:
#	ssh root@debbi "cd /var/local/nginx/deploy.arcusx.lan/;./update*"
