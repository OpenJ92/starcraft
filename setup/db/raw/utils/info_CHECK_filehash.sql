select
	filehash
from
	"replay"."INFO"
where
	filehash = '{filehash}'
limit 1
;
