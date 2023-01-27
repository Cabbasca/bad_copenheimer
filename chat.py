"""
Dumps the data pack info from the "join_game" packet to a file.

Supports Minecraft 1.16.3+.
"""

# from __future__ import print_function
import builtins
import twisted
from twisted.internet import reactor, defer
from quarry.types.nbt import NBTFile, alt_repr
from quarry.net.client import ClientFactory, ClientProtocol
from quarry.net.auth import ProfileCLI
import quarry

flag = False

class DataPackDumperProtocol(ClientProtocol):
    def packet_join_game(self, buff):
        entity_id, is_hardcore, gamemode, prev_gamemode = buff.unpack('i?bb')
        dimension_names = [buff.unpack_string() for _ in range(buff.unpack_varint())]
        data_pack = buff.unpack_nbt()
        buff.discard()  # Ignore the test of the packet

        if self.factory.output_path:
            try:
                data_pack = NBTFile(data_pack)
                data_pack.save(self.factory.output_path)
            except builtins.KeyError:
                pass
        else:
            # print(alt_repr(data_pack))
            global flag
            flag = True
            quit()

        quit()


class DataPackDumperFactory(ClientFactory):
    try:
        protocol = DataPackDumperProtocol
    except quarry.net.client.ClientProtocol:
        pass
    except Exception:
        pass


@defer.inlineCallbacks # type: ignore
def run(args):
    # Log in
    profile = yield ProfileCLI.make_profile(args)

    # Create factory
    factory = DataPackDumperFactory(profile)
    factory.output_path = args.output_path

    # Connect!
    try:
        factory.connect(args.host, args.port)
    except quarry.net.client.ClientProtocol:
        pass
    except Exception:
        pass


def main(argv):
    parser = ProfileCLI.make_parser()
    parser.add_argument("host")
    parser.add_argument("-p", "--port", default=25565, type=int)
    parser.add_argument("-o", "--output-path")
    args = parser.parse_args(argv)


    run(args)
    try:
        reactor.callLater(10, quit) # type: ignore
        reactor.run() # type: ignore
    except builtins.ValueError:
        quit()
    except twisted.internet.error.ReactorNotRunning: # pyright: ignore[reportGeneralTypeIssues]
        pass
    except Exception:
        pass


def quit():
    try:
        reactor.stop() # type: ignore
    except twisted.internet.error.ReactorNotRunning: # pyright: ignore[reportGeneralTypeIssues]
        pass
    except Exception:
        pass

if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
