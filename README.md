# VMI API

API for obtaining results from the Beery-Bukenica test of the visomotor integration development (VMI) 4th edition.

## Install
```
docker-compose up --build -d
```

By default, the application is displayed listening to port ** 8000 **. You can change the ports by editing the ** docker-compose.yml ** file.

## API docs
```
http://localhost:8000/docs
http://localhost:8000/redoc
```

### URL example
```
http://localhost:8000/vmi?age_years=4&age_months=10&vmi_natural_scores=18&visual_natural_scores=16&motor_natural_scores=24
```


## References
- Beery, K. E. (1989). Developmental test of visual-motor integration: Administration, scoring and teaching manual. Modern Curriculum Press (4th edition).
