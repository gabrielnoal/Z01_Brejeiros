library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Mux4Way is
	port ( 
			a:   in  STD_LOGIC;
			b:   in  STD_LOGIC;
			c:   in  STD_LOGIC;
			d:   in  STD_LOGIC;
			sel: in  STD_LOGIC_VECTOR(1 downto 0);
			q:   out STD_LOGIC);
end entity;

architecture rtl of Mux4Way is
begin
	process (sel,a,b,c,d)
	begin
		case sel is
			when b"00" => q<=a;
			when b"01" => q<=b;
			when b"10" => q<=c;
			when others => q<=d;
		end case;
	end process;
end rtl;
