\copy (SELECT nm.id          , nm.value       , nm.unit        , nm.type        , nm.doc_char_begin, nm.doc_char_end, nm.token_begin , nm.token_end   , nm.sentence_id , s.id            , s.doc_id        , s.sentence_index, s.gloss         , s.words         , s.lemmas        , s.pos_tags      , s.ner_tags      , s.doc_char_begin, s.doc_char_end  , s.dependencies  FROM cc_numericmention AS nm, javanlp_sentence AS s WHERE nm.sentence_id = s.id) TO '/home/chaganty/Research/contextual-comparatives/mentions.tsv' WITH DELIMITER E'\t';

\copy (SELECT * FROM cc_numericdata AS nd) TO '/home/chaganty/Research/contextual-comparatives/numeric_data.tsv' WITH DELIMITER E'\t';