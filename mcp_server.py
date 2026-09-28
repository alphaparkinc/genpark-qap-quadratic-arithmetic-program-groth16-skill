import sys
import json
from client import QAPReduction

qap = QAPReduction()

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "qap_identity_check",
                        "description": "Check QAP divisibility identity A(x)*B(x) - C(x) = H(x)*T(x)",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "a_eval": {"type": "integer"},
                                "b_eval": {"type": "integer"},
                                "c_eval": {"type": "integer"},
                                "x": {"type": "integer"},
                                "roots": {"type": "array", "items": {"type": "integer"}}
                            },
                            "required": ["a_eval", "b_eval", "c_eval", "x"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "qap_identity_check":
            r = args.get("roots", [1, 2])
            red = QAPReduction(roots=r)
            ok = red.check_qap_identity(args["a_eval"], args["b_eval"], args["c_eval"], args["x"])
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"qap_valid": ok})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
