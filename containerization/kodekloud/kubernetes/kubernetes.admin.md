# Kubernetes Administration

## Useful links

- Certified Kubernetes Administrator [https://www.cncf.io/certification/cka/]
- Candidate Handbook: [https://www.cncf.io/certification/candidate-handbook]
- Exam Tips: [http://training.linuxfoundation.org/go//Important-Tips-CKA-CKA]

Use the code – DEVOPS15 – while registering for the CKA or CKAD exams at Linux Foundation to get a 15% discount.

## Recall

- Kube API-Server

It's an HTTP(TCP) server for managing kubernetes objects. It's the only component that interact with the ETCD key-value store.
All other component along with external application pass through the Api-Server to query for information in the etcd storage.
