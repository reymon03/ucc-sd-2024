CREATE USER replicator WITH REPLICATION ENCRYPTED PASSWORD 'replicator_password';
SELECT pg_create_physical_replication_slot('replication_slot');

CREATE TABLE productos (
    id serial4 PRIMARY KEY,
    nombre_producto VARCHAR(100),
    precio DECIMAL,
    categoria VARCHAR(50)
);
    
CREATE TABLE clientes (
	id serial4 NOT NULL,
	nombre_cliente varchar(100) NULL,
	correo varchar(100) NULL,
	edad int4 NULL,
	CONSTRAINT clientes_pkey PRIMARY KEY (id)
);