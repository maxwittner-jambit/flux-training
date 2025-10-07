## Kubernetes (Minikube) project

- Title: Hogwarts Magic School Student Registration App
- Author: Kavindu Kalinga
- Languages: `python3` , `HTML`
- Framework: `Flask`
- Databse: `postgreSQL`
- Containerization tools and APIs: `Docker` `kubernetes` `minikube`
- Reference: YouTube: [Flask app with PostgreSQL](https://www.youtube.com/watch?v=XZ_gAWdGzZk)  

### CMD

```bash
# Deploy DB
kubectl apply -f postgres-cm.yml
kubectl apply -f postgres-deployment.yml
kubectl apply -f postgres-sec.yml

# Deploy app
kubectl apply -f hogwartzapp.yml

# Visit Launched App
minikube service hogwartzapp
```

### Credentials

```bash
# POSTGRES_USER
echo "cG9zdGdyZXM=" | base64 --decode; echo

# POSTGRES_PASSWORD
echo "cG9zdGdyZXM=" | base64 --decode; echo

```

### Verification

```bash
# Verify cluster
kubectl get pods
kubectl get svc
kubectl get deploy
```

```bash
# Verify DB
(base) kkalinga@ISA-KKALINGA:~$ k get pods -w
NAME                        READY   STATUS              RESTARTS   AGE
postgres-58c77d6988-9wgpc   0/1     ContainerCreating   0          42s
postgres-58c77d6988-9wgpc   1/1     Running             0          70s
^C

(base) kkalinga@ISA-KKALINGA:~$ k get pods
NAME                        READY   STATUS    RESTARTS   AGE
postgres-58c77d6988-9wgpc   1/1     Running   0          83s

(base) kkalinga@ISA-KKALINGA:~$ k exec -it postgres-58c77d6988-9wgpc bash

root@postgres-58c77d6988-9wgpc:/# psql -n postgres -U postgres
psql (16.2 (Debian 16.2-1.pgdg120+2))
Type "help" for help.

postgres=# \l
postgres=# \c students
You are now connected to database "students" as user "postgres".

# Before creating DB using App
students=# \dt
Did not find any relations.

# After Creating DB using App
students=# \dt
          List of relations
 Schema |   Name   | Type  |  Owner   
--------+----------+-------+----------
 public | students | table | postgres
(1 row)

students=# select * from students;
 id |  fname  |  lname  | pet 
----+---------+---------+-----
  1 | Kavindu | Kalinga | owl
(1 row)

students=# select * from students;
 id |  fname  |  lname  | pet 
----+---------+---------+-----
  1 | Kavindu | Kalinga | owl
  2 | harry   | potter  | owl
  3 | isa     | cmb     | cat
  4 | ron     | weasley | rat
(4 rows)

```

### Clear the cluster

```bash
kubectl get all
kubectl delete all --all
```
