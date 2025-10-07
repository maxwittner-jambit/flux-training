## Kubernetes (Minikube) project

- Title: Todo - Task writing App
- Author: Kavindu Kalinga
- Languages: `python3` , `HTML`
- Framework: `Django`
- Databse: `postgreSQL`
- Containerization tools and APIs: `Docker` `kubernetes` `minikube`
- Reference:
  - YouTube:
    - [Build Django To-Do App with PostgreSQL](https://youtu.be/Nnoxz9JGdLU?si=s_GEqClwIGInNs9i)
    - [Docker volumes](https://www.youtube.com/watch?v=eJrR1X38pk4)
    - [Pagination](https://www.youtube.com/watch?v=N-PB-HMFmdo)

### CMD

```bash
# Deploy DB
kubectl apply -f postgres-cm.yml
kubectl apply -f postgres-deployment.yml
kubectl apply -f postgres-sec.yml

# Deploy app
kubectl apply -f k8swebapp.yml

# Visit Launched App
minikube service k8swebapp

```

### Credentials

```bash
# POSTGRES_USER
echo "cG9zdGdyZXM=" | base64 --decode; echo

# POSTGRES_PASSWORD
echo "cG9zdGdyZXM=" | base64 --decode; echo

```

### Initialization

```bash
kubectl get pods
kubectl exec -it k8s-kkwebapp-65f968bb48-bjc97 bash
>>> python3 manage.py migrate
>>> python3 manage.py runserver
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
base) kkalinga@ISA-KKALINGA:~$ k get pods
NAME                            READY   STATUS    RESTARTS   AGE
k8s-kkwebapp-65f968bb48-bjc97   1/1     Running   0          76s
k8s-kkwebapp-65f968bb48-bp74n   1/1     Running   0          76s
k8s-kkwebapp-65f968bb48-gjswt   1/1     Running   0          76s
postgres2-54b8b4846c-rgjsz      1/1     Running   0          76s
(base) kkalinga@ISA-KKALINGA:~$ k exec -it postgres2-54b8b4846c-rgjsz bash
kubectl exec [POD] [COMMAND] is DEPRECATED and will be removed in a future version. Use kubectl exec [POD] -- [COMMAND] instead.
root@postgres2-54b8b4846c-rgjsz:/# psql -n postgres -U postgres

postgres=# \l
                                                      List of databases
   Name    |  Owner   | Encoding | Locale Provider |  Collate   |   Ctype    | ICU Locale | ICU Rules |   Access privileges   
-----------+----------+----------+-----------------+------------+------------+------------+-----------+-----------------------
 TodoDB    | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 postgres  | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | 
 template0 | postgres | UTF8     | libc            | en_US.utf8 | en_US.utf8 |            |           | =c/postgres          +
.
.
...
(4 rows)

postgres=# \c "TodoDB"
You are now connected to database "TodoDB" as user "postgres".
TodoDB=# \dt
                   List of relations
 Schema |            Name            | Type  |  Owner   
--------+----------------------------+-------+----------
 public | auth_group                 | table | postgres
 public | auth_group_permissions     | table | postgres
 public | auth_permission            | table | postgres
 public | auth_user                  | table | postgres
 public | auth_user_groups           | table | postgres
 public | auth_user_user_permissions | table | postgres
 public | django_admin_log           | table | postgres
 public | django_content_type        | table | postgres
 public | django_migrations          | table | postgres
 public | django_session             | table | postgres
 public | todos_todo                 | table | postgres
(11 rows)

TodoDB=# select * from todos_todo;
 id | content 
----+---------
  1 | isa
  3 | kalinga
  4 | cmb
  5 | java
  6 | python
  7 | js
  8 | c++
 11 | html
(8 rows)

```

### Clear the cluster

```bash
kubectl get all
kubectl delete all --all
```
