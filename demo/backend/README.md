```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: fastapi-weather
  labels:
    app: fastapi-weather
spec:
  replicas: 3
  selector:
    matchLabels:
      app: fastapi-weather
  template:
    metadata:
      labels:
        app: fastapi-weather
    spec:
      containers:
        - name: fastapi-weather
          image: yingjunluo/fastapi-weather:v1.0
          ports:
            - containerPort: 8000
              protocol: TCP
          env:
            - name: API_KEY
              value: "fc15ed0082ac433cdcfb87dbcf8bb3b3"
```