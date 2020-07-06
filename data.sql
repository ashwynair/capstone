--
-- PostgreSQL database dump
--

-- Dumped from database version 11.5
-- Dumped by pg_dump version 11.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: Actors; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Actors" (
    actor_id integer NOT NULL,
    name character varying(120) NOT NULL,
    age integer NOT NULL,
    gender character varying(1) NOT NULL
);


ALTER TABLE public."Actors" OWNER TO postgres;

--
-- Name: Actors_actor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Actors_actor_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Actors_actor_id_seq" OWNER TO postgres;

--
-- Name: Actors_actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Actors_actor_id_seq" OWNED BY public."Actors".actor_id;


--
-- Name: Movies; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Movies" (
    movie_id integer NOT NULL,
    title character varying(120) NOT NULL,
    release_date timestamp without time zone NOT NULL
);


ALTER TABLE public."Movies" OWNER TO postgres;

--
-- Name: Movies_movie_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Movies_movie_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Movies_movie_id_seq" OWNER TO postgres;

--
-- Name: Movies_movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Movies_movie_id_seq" OWNED BY public."Movies".movie_id;


--
-- Name: Roles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Roles" (
    role_id integer NOT NULL,
    actor_id integer NOT NULL,
    movie_id integer NOT NULL,
    role_desc character varying(120)
);


ALTER TABLE public."Roles" OWNER TO postgres;

--
-- Name: Roles_role_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Roles_role_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Roles_role_id_seq" OWNER TO postgres;

--
-- Name: Roles_role_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Roles_role_id_seq" OWNED BY public."Roles".role_id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: Actors actor_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actors" ALTER COLUMN actor_id SET DEFAULT nextval('public."Actors_actor_id_seq"'::regclass);


--
-- Name: Movies movie_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Movies" ALTER COLUMN movie_id SET DEFAULT nextval('public."Movies_movie_id_seq"'::regclass);


--
-- Name: Roles role_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Roles" ALTER COLUMN role_id SET DEFAULT nextval('public."Roles_role_id_seq"'::regclass);


--
-- Data for Name: Actors; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Actors" (actor_id, name, age, gender) FROM stdin;
1	Ashwyn Nair	22	M
2	Actor 2	123	F
3	Actor 3	11	F
4	Actor 4	20	M
5	Actor 5	44	F
\.


--
-- Data for Name: Movies; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Movies" (movie_id, title, release_date) FROM stdin;
1	Movie 1	2020-12-01 00:00:00
2	Movie 2	2000-10-23 00:00:00
3	Movie 3	2004-05-24 00:00:00
4	Movie 5	2010-01-29 00:00:00
5	Movie 6	2014-05-19 00:00:00
\.


--
-- Data for Name: Roles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Roles" (role_id, actor_id, movie_id, role_desc) FROM stdin;
\.


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
f77f759edb07
\.


--
-- Name: Actors_actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Actors_actor_id_seq"', 5, true);


--
-- Name: Movies_movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Movies_movie_id_seq"', 5, true);


--
-- Name: Roles_role_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Roles_role_id_seq"', 1, false);


--
-- Name: Actors Actors_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Actors"
    ADD CONSTRAINT "Actors_pkey" PRIMARY KEY (actor_id);


--
-- Name: Movies Movies_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Movies"
    ADD CONSTRAINT "Movies_pkey" PRIMARY KEY (movie_id);


--
-- Name: Roles Roles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Roles"
    ADD CONSTRAINT "Roles_pkey" PRIMARY KEY (role_id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: Roles Roles_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Roles"
    ADD CONSTRAINT "Roles_actor_id_fkey" FOREIGN KEY (actor_id) REFERENCES public."Actors"(actor_id);


--
-- Name: Roles Roles_movie_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Roles"
    ADD CONSTRAINT "Roles_movie_id_fkey" FOREIGN KEY (movie_id) REFERENCES public."Movies"(movie_id);


--
-- PostgreSQL database dump complete
--

