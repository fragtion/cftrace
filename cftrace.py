import argparse
import requests
import json

def parse_args():
    parser = argparse.ArgumentParser(description="Process traceroute results.")
    parser.add_argument("-targets", required=True, help="Comma-separated list of targets")
    parser.add_argument("-colos", required=True, help="Comma-separated list of colos")
    parser.add_argument("-packet_type", default="udp", help="Packet type (default: udp)")
    return parser.parse_args()

def fetch_traceroute_data(targets, colos, packet_type):
    url = "https://faizazhar.com/projects/traceroute"
    params = {
        "targets": targets,
        "colos": colos,
        "packet_type": packet_type
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def format_traceroute(result):
    output = []
    max_ttl_length = 0
    max_ip_length = 0
    entries = []

    if 'result' not in result:
        print("No results found.")
        return ""

    # Group results by datacenter and target
    dc_results = {}

    for entry in result['result']:
        for colo in entry['colos']:
            colo_name = colo['colo']['name']
            if colo_name not in dc_results:
                dc_results[colo_name] = {}

            for hop in colo['hops']:
                for node in hop['nodes']:
                    ip = node['ip'] or "*"
                    name = node['name'] or "-"
                    ttl_length = len(str(hop['packets_ttl']))
                    ip_length = len(ip)
                    name_length = len(name)
                    length = ip_length + name_length + 3  # Account for ( and ) and space
                    if ttl_length > max_ttl_length:
                        max_ttl_length = ttl_length
                    if length > max_ip_length:
                        max_ip_length = length

                    if entry['target'] not in dc_results[colo_name]:
                        dc_results[colo_name][entry['target']] = []

                    dc_results[colo_name][entry['target']].append({
                        'ttl': hop['packets_ttl'],
                        'name': name,
                        'ip': ip,
                        'mean_rtt': f"{node['mean_rtt_ms']:.2f}",
                        'min_rtt': f"{node['min_rtt_ms']:.2f}",
                        'max_rtt': f"{node['max_rtt_ms']:.2f}",
                        'packet_count': node.get('packet_count', 0)
                    })

    # Format the output with proper alignment
    for dc, targets in dc_results.items():
        output.append(f"{dc}:")
        for target, lines in targets.items():
            output.append(f"  {target}")
            for hop in lines:
                ttl_field = f"{hop['ttl']}".rjust(max_ttl_length)
                if hop['name'] == "NO RESPONSE":
                    formatted_ip = f"{hop['ip']}"
                    rtt_field = f"!X"
                else:
                    formatted_ip = f"{hop['name']} ({hop['ip']})"
                    rtt_field = f"{hop['mean_rtt']}ms ({hop['min_rtt']}~{hop['max_rtt']}, count={hop['packet_count']})"
                ip_field = formatted_ip.ljust(max_ip_length)
                output.append(f"  {ttl_field}   {ip_field} {rtt_field}")
    return "\n".join(output)

def main():
    args = parse_args()
    result = fetch_traceroute_data(args.targets, args.colos, args.packet_type)
    if result and result['success']:
        formatted_output = format_traceroute(result)
        print(formatted_output)
    else:
        print("Failed to retrieve traceroute data.")

if __name__ == "__main__":
    main()
