--
-- PostgreSQL database dump
--

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
-- PostgreSQL database dump complete
--

