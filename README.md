# versioned (Version Editor) - a version number tool

versioned is a command line tool to work with version numbers. Features include

- check if version number matches the version number format
- removal of "-SNAPSHOT" suffix
- calculation of next release or development versions.

## Version number formats

versioned supports semantic versions of the form 1.2.3-SNAPSHOT for now. This
format is known from maven (a popular java build tool) and is called 'mvn'. The
format option `-f mvn` can be omitted as for now `mvn` is the default.

### Test if version matches format
```
versioned -f mvn -c isVersion 1
true
```

```
versioned -f mvn -c isVersion foo
false
```

### Test if version is a development version
```
versioned -f mvn -c isSnapshot 1-SNAPSHOT
true
```

```
versioned -f mvn -c isSnapshot 1
false
```
### Test if version is a release version
```
versioned -f mvn -c isRelease 1-SNAPSHOT
false
```

```
versioned -f mvn -c isRelease 1
true
```

### Calculate next release version based on development version
```
versioned -f mvn -c nextRelease 1.2.3-SNAPSHOT
1.2.3
```

### Calculate next development version based on release version
```
versioned -f mvn -c nextSnapshot 1.2.3
1.2.4-SNAPSHOT
```

## License

[MIT License](LICENSE.txt)
